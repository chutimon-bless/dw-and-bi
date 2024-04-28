import glob
import json
import os
from typing import List

# lib ของ python ที่เอาไว้เชื่อมกับ postgres
import psycopg2


def get_files(filepath: str) -> List[str]:
    """
    Description: This function is responsible for listing the files in a directory
    """

    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, "*.json"))
        for f in files:
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print(f"{num_files} files found in {filepath}")

    return all_files


def process(cur, conn, filepath):
    # Get list of files from filepath
    all_files = get_files(filepath)

    for datafile in all_files:
        with open(datafile, "r") as f:
            data = json.loads(f.read())
            for each in data:
                # Print some sample data
                
                # if each["type"] == "IssueCommentEvent":
                #     print(
                #         each["id"], 
                #         each["type"],
                #         each["actor"]["id"],
                #         each["actor"]["login"],
                #         each["repo"]["id"],
                #         each["repo"]["name"],
                #         each["created_at"],
                #         each["payload"]["issue"]["url"],
                #     )
                # else:
                #     print(
                #         each["id"], 
                #         each["type"],
                #         each["actor"]["id"],
                #         each["actor"]["login"],
                #         each["repo"]["id"],
                #         each["repo"]["name"],
                #         each["created_at"],
                #     )

                # Insert data into tables here
                insert_statement = f"""
                    INSERT INTO actors (
                        id,
                        login
                    ) VALUES ({each["actor"]["id"]}, '{each["actor"]["login"]}')
                    ON CONFLICT (id) DO NOTHING
                """
                # print(insert_statement)
                cur.execute(insert_statement)

                # Insert data into tables here
                insert_statement = f"""
                    INSERT INTO repo (
                        id,
                        name
                    ) VALUES ({each["repo"]["id"]}, '{each["repo"]["name"]}')
                    ON CONFLICT (id) DO NOTHING
                """
                # print(insert_statement)
                cur.execute(insert_statement)

                # Insert data into tables here
                insert_statement = f"""
                    INSERT INTO events (
                        event_id,
                        actor_id,
                        repo_id,
                        type,
                        created_at
                    ) VALUES ('{each["id"]}', '{each["actor"]["id"]}','{each["repo"]["id"]}', '{each["type"]}', '{each["created_at"]}')
                    ON CONFLICT (event_id) DO NOTHING
                """
                # print(insert_statement)
                cur.execute(insert_statement)

                conn.commit()


def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=postgres"
    )
    cur = conn.cursor()

# .. คือ ออกมา 1 ชั้น (ตอนนี้อยู่ใน 01-data-modeling) แล้วเข้าไปยัง folder data
    process(cur, conn, filepath="../data")

    conn.close()


if __name__ == "__main__":
    main()