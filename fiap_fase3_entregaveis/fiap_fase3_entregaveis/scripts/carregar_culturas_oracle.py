"""Carga repetível de produtos_agricolas.csv para CULTURAS_AGRICOLAS.

Dependências: py -m pip install pandas oracledb
Variáveis: ORACLE_USER, ORACLE_PASSWORD e ORACLE_DSN.
ATENÇÃO: substitui os registros atuais da tabela de trabalho CULTURAS_AGRICOLAS.
"""

import os
import sys
from pathlib import Path

import pandas as pd
import oracledb

CSV_PATH = Path(__file__).resolve().parents[1] / "produtos_agricolas.csv"
REQUIRED = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall", "label"]


def read_and_validate_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"CSV não encontrado: {path}")
    df = pd.read_csv(path)
    df.columns = [str(c).strip() for c in df.columns]
    by_lower = {str(c).lower(): c for c in df.columns}
    missing = [c for c in REQUIRED if c not in by_lower]
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {missing}")
    df = df[[by_lower[c] for c in REQUIRED]].copy()
    df.columns = REQUIRED
    df = df.drop_duplicates()
    for col in REQUIRED[:-1]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df["label"] = df["label"].astype("string").str.strip()
    df = df.dropna(subset=["label"])
    df = df[df["label"] != ""]
    return df


def main() -> int:
    user = os.getenv("ORACLE_USER")
    password = os.getenv("ORACLE_PASSWORD")
    dsn = os.getenv("ORACLE_DSN")
    if not all([user, password, dsn]):
        print("Configure ORACLE_USER, ORACLE_PASSWORD e ORACLE_DSN.", file=sys.stderr)
        return 2

    df = read_and_validate_csv(CSV_PATH)
    print(f"Registros válidos preparados: {len(df)}")
    sql = """INSERT INTO CULTURAS_AGRICOLAS
        (N, P, K, TEMPERATURA, UMIDADE, PH, PRECIPITACAO, CULTURA)
        VALUES (:1, :2, :3, :4, :5, :6, :7, :8)"""

    rows = []
    for row in df.itertuples(index=False, name=None):
        vals = [None if pd.isna(v) else v for v in row]
        rows.append(tuple(vals))

    conn = None
    try:
        conn = oracledb.connect(user=user, password=password, dsn=dsn)
        with conn.cursor() as cur:
            # DELETE e INSERT são confirmados juntos; em caso de erro ocorre rollback.
            cur.execute("DELETE FROM CULTURAS_AGRICOLAS")
            if rows:
                cur.executemany(sql, rows)
            cur.execute("SELECT COUNT(*) FROM CULTURAS_AGRICOLAS")
            total = cur.fetchone()[0]
        conn.commit()
        print(f"Carga concluída. Total na tabela: {total}")
        return 0
    except Exception:
        if conn is not None:
            conn.rollback()
        raise
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
