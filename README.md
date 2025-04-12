# Student Dashboard

A personal productivity dashboard for students built with vanilla JavaScript.

## Features

### To-Do List
- Add, edit, and delete tasks
- Mark tasks as completed
- Filter tasks by status (All, Active, Completed)
- Tasks are sorted by creation date (newest first)

### Class Schedule
- Add classes with name, time, duration, and location
- View schedule by day of the week
- Edit and delete classes
- Classes are sorted by time

### Quick Notes
- Create notes with title and content
- Edit and delete notes
- Notes are sorted by creation date (newest first)

### Real-time Clock & Date
- Displays current time and date
- Updates in real-time

## Technical Implementation

### ES6+ Features Used

1. **let & const**
   - Used throughout the code for proper variable declarations
   - `const` for values that don't change
   - `let` for variables that need reassignment

2. **Arrow Functions**
   - Used for event handlers and callbacks
   - Example: `setInterval(() => { ... }, 1000)`
   - Example: `filterButtons.forEach(button => { ... })`

3. **Template Literals**
   - Used for dynamic HTML rendering
   - Example: `` `<div class="note-title">${this.escapeHtml(note.title)}</div>` ``

4. **Async/Await**
   - Used for simulated data fetching
   - Example: `async fetchWeatherData() { ... }`
   - Example: `const weatherData = await app.fetchWeatherData()`

5. **Classes**
   - Main `Dashboard` class to organize code and manage state
   - Methods for handling different features

6. **Destructuring**
   - Used for extracting values from arrays
   - Example: `const [hours, minutes] = time24h.split(':')`

7. **Spread Operator**
   - Used for creating copies of arrays
   - Example: `let filteredTodos = [...this.todos]`

8. **Default Parameters**
   - Used in some function definitions

9. **localStorage API**
   - Used for persistent data storage
   - JSON.stringify/parse for data serialization

## Data Storage

All data is stored in the browser's localStorage:
- To-Do items
- Class schedule
- Notes

## Screenshots

![Dashboard Overview](dashboard-overview.png)
![To-Do List](todo-list.png)
![Class Schedule](class-schedule.png)
![Quick Notes](quick-notes.png)

## How to Run

1. Download all files (index.html, styles.css, app.js)
2. Open index.html in any modern browser
3. No build steps or dependencies required

## Browser Compatibility

Works in all modern browsers that support ES6+ features:
- Chrome
- Firefox
- Safari
- Edge
