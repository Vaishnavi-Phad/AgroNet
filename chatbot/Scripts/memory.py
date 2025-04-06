# memory.py
import sqlite3

def init_db():
    conn = sqlite3.connect('chat_memory.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 agent TEXT,
                 message TEXT,
                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def save_message(agent, message):
    conn = sqlite3.connect('chat_memory.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (agent, message) VALUES (?, ?)", (agent, message))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect('chat_memory.db')
    c = conn.cursor()
    c.execute("SELECT agent, message, timestamp FROM messages ORDER BY timestamp ASC")
    messages = c.fetchall()
    conn.close()
    return messages
