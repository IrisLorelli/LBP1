import sqlite3

class Personagem:
    # Nome do arquivo de banco de dados SQLite
    DB_NAME = 'database.db'

    def __init__(self, nome=None, elemento=None, arma=None, raridade=None, id=None):
        self.id = id
        self.nome = nome
        self.elemento = elemento
        self.arma = arma
        self.raridade = raridade

    @classmethod
    def get_connection(cls):
#        """Conecta ao banco SQLite nativo e permite acessar colunas por nome."""
        conn = sqlite3.connect(cls.DB_NAME)
        conn.row_factory = sqlite3.Row
        return conn

    @classmethod
    def criar_tabela(cls):
#        """Cria a tabela de personagens com SQL puro (CREATE TABLE)."""
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS personagens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                elemento TEXT NOT NULL,
                arma TEXT NOT NULL,
                raridade INTEGER NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def salvar(self):
#        """Insere o registro no banco com SQL puro (INSERT INTO)."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO personagens (nome, elemento, arma, raridade)
            VALUES (?, ?, ?, ?)
        ''', (self.nome, self.elemento, self.arma, self.raridade))
        conn.commit()
        conn.close()

    @classmethod
    def buscar_todos(cls):
#        """Recupera todos os registros no banco com SQL puro (SELECT)."""
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, elemento, arma, raridade FROM personagens')
        linhas = cursor.fetchall()
        conn.close()

        # Converte o resultado em instâncias do modelo
        personagens = []
        for linha in linhas:
            p = cls(
                id=linha['id'],
                nome=linha['nome'],
                elemento=linha['elemento'],
                arma=linha['arma'],
                raridade=linha['raridade']
            )
            personagens.append(p)
        return personagens