<h1>📚 CLI Library Manager</h1>

<p>A simple CLI-based Library Manager written in Python that allows users to add, remove, search, display, and manage books in a JSON-based library.</p>

<h2>🚀 Features</h2>

<ul>
  <li>➕ Add books with title, author, year, genre, and read status.</li>
  <li>🗑️ Remove books from the library by title.</li>
  <li>🔍 Search books by title or author.</li>
  <li>📚 Display all books in the library.</li>
  <li>📊 View statistics including total books and read percentage.</li>
  <li>💾 Saves data persistently in <code>library.json</code>.</li>
</ul>

<h2>📦 Installation</h2>

<ol>
  <li>Clone this repository:</li>
  <pre><code>git clone https://github.com/your-repo/library-manager.git
cd library-manager
  </code></pre>

  <li>Install required dependencies (if any):</li>
  <pre><code>pip install -r requirements.txt</code></pre>

  <li>Run the program:</li>
  <pre><code>python library_manager.py</code></pre>
</ol>

<h2>🛠 Usage</h2>

<p>Once you run the program, you will see a menu:</p>

<pre>
--------------------📚 Welcome to your Personal Library Manager! --------------------
1. ➕ Add a book
2. 🗑️ Remove a book
3. 🔍 Search for a book
4. 📚 Display all books
5. 📊 Display statistics
6. 🚪 Exit
</pre>

<p>Follow the on-screen prompts to manage your library!</p>

<h2>📂 Data Storage</h2>

<p>The library is stored in <code>library.json</code> for persistence. Make sure the file is in the same directory as the script.</p>

<h2>🔧 Customization</h2>

<p>If you want to modify the storage location, update the <code>LIBRARY_FILE</code> variable in the script:</p>

<pre><code>import os

LIBRARY_FILE = os.path.join(os.path.expanduser("~"), "Documents", "library.json")
</code></pre>

<p>This will store the file in the user's <code>Documents</code> folder.</p>

<h2>🤝 Contributing</h2>

<p>Feel free to submit issues or pull requests to improve this project.</p>

<h2>📜 License</h2>

<p>This project is open-source. Feel free to use and modify it.</p>
