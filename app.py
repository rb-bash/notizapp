from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import json

app = Flask(__name__)
socketio = SocketIO(app)

def load_notes():
    try:
        with open('notes.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Gibt eine leere Liste zurück, wenn die Datei nicht existiert

def save_notes(notes):
    with open('notes.json', 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    notes = load_notes()  # Lade die Notizen direkt hier
    return render_template('index.html', notes=notes)

@socketio.on('add_note')
def handle_add_note(data):
    notes = load_notes()  # Lade die Notizen beim Hinzufügen
    notes.append(data)
    save_notes(notes)  # Speichere die Notizen in der Datei
    emit('update_notes', notes, broadcast=True)

@socketio.on('toggle_note')
def handle_toggle_note(data):
    notes = load_notes()  # Lade die Notizen beim Umschalten
    index = data['index']
    notes[index]['completed'] = not notes[index]['completed']
    save_notes(notes)  # Speichere die Notizen in der Datei
    emit('update_notes', notes, broadcast=True)

@socketio.on('delete_note')
def handle_delete_note(data):
    notes = load_notes()  # Lade die Notizen beim Löschen
    index = data['index']
    if 0 <= index < len(notes):
        del notes[index]  # Lösche die Notiz an der angegebenen Stelle
        save_notes(notes)  # Speichere die aktualisierten Notizen in der Datei
    emit('update_notes', notes, broadcast=True)

@socketio.on('add_subnote')
def handle_add_subnote(data):
    notes = load_notes()  # Lade die Notizen beim Hinzufügen von Unternotizen
    index = data['index']
    subnote = data['subnote']
    
    if 0 <= index < len(notes):
        if 'subnotes' not in notes[index]:
            notes[index]['subnotes'] = []
        notes[index]['subnotes'].append(subnote)
        save_notes(notes)  # Speichere die Notizen in der Datei
    emit('update_notes', notes, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)