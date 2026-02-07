from flask import Flask, request

app= Flask(__name__)
notes= []

@app.route("/")
def home():
    return """
<h1>Notes online app</h1>
<form action="/add" method="post">
<input type="text" name="note" placeholder="write a note: " required>
<button type="submit">Submit</button>
</form>
<h2> Saved notes: </h2>
""" + "<br>".join(notes)

@app.route("/add", methods=["POST"])
def add_note():
    note= request.form["note"]
    notes.append(note)
    return home()

if __name__ == "__main__":
    app.run(debug=True)