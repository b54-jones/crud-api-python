from sqlalchemy import create_engine, text
from User import User
import json

def execute_query(query):
    conn_str = "oracle+oracledb://ben:password@localhost:1521/?service_name=xe"

    engine = create_engine(conn_str)

    with engine.connect() as conn:
        result = conn.execute(text(query))

        if not result.returns_rows:
            row_count = result.rowcount
            conn.commit()
            return json.dumps({
                "message": "Query executed successfully",
                "rows_affected": row_count
            }, indent=2)

        columns = result.keys()
        rows = result.fetchall()
        data = [dict(zip(columns, row)) for row in rows]
        return json.dumps(data, indent=2, default=str)