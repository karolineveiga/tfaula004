from mysql import connector

db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'basedeAlunos'
}

def init_db():
    connection = connector.connect(**db_config)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Alunos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100),
            idade INT,
            média FLOAT
        )
    """)

    example_data = [
        ('Alice', 20, 8.5),
        ('Bob', 22, 7.0),
        ('Charlie', 19, 9.2)
    ]

    cursor.executemany("""
        INSERT INTO Alunos (nome, idade, média) VALUES (%s, %s, %s)
    """, example_data)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    init_db()