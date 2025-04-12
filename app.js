// Main App Class
class Dashboard {
  constructor() {
    this.todos = JSON.parse(localStorage.getItem("todos")) || []
    this.schedule = JSON.parse(localStorage.getItem("schedule")) || []
    this.notes = JSON.parse(localStorage.getItem("notes")) || []
    this.currentFilter = "all"
    this.currentDay = "Monday"

    this.initializeTabs()
    this.initializeDateTime()
    this.initializeTodoList()
    this.initializeSchedule()
    this.initializeNotes()
  }

  // Initialize tab navigation
  initializeTabs() {
    const tabButtons = document.querySelectorAll(".tab-btn")
    const tabContents = document.querySelectorAll(".tab-content")

    tabButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const tabId = button.dataset.tab

        // Remove active class from all buttons and contents
        tabButtons.forEach((btn) => btn.classList.remove("active"))
        tabContents.forEach((content) => content.classList.remove("active"))

        // Add active class to clicked button and corresponding content
        button.classList.add("active")
        document.getElementById(tabId).classList.add("active")
      })
    })
  }

  // Initialize real-time date and time
  initializeDateTime() {
    const updateDateTime = () => {
      const now = new Date()

      // Update time
      const timeElement = document.getElementById("time")
      timeElement.textContent = now.toLocaleTimeString("en-US", {
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: true,
      })

      // Update date
      const dateElement = document.getElementById("date")
      dateElement.textContent = now.toLocaleDateString("en-US", {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric",
      })
    }

    // Update immediately and then every second
    updateDateTime()
    setInterval(updateDateTime, 1000)
  }

  // Initialize To-Do List functionality
  initializeTodoList() {
    const todoForm = document.getElementById("todo-form")
    const todoInput = document.getElementById("todo-input")
    const todoList = document.getElementById("todo-list")
    const filterButtons = document.querySelectorAll(".filter-btn")

    // Render initial todos
    this.renderTodos()

    // Add new todo
    todoForm.addEventListener("submit", (e) => {
      e.preventDefault()

      const todoText = todoInput.value.trim()
      if (todoText) {
        const newTodo = {
          id: Date.now(),
          text: todoText,
          completed: false,
          createdAt: new Date().toISOString(),
        }

        this.todos.push(newTodo)
        this.saveTodos()
        this.renderTodos()

        todoInput.value = ""
      }
    })

    // Filter todos
    filterButtons.forEach((button) => {
      button.addEventListener("click", () => {
        filterButtons.forEach((btn) => btn.classList.remove("active"))
        button.classList.add("active")

        this.currentFilter = button.dataset.filter
        this.renderTodos()
      })
    })

    // Handle todo actions (complete, edit, delete)
    todoList.addEventListener("click", (e) => {
      const todoItem = e.target.closest(".todo-item")
      if (!todoItem) return

      const todoId = Number(todoItem.dataset.id)
      const todo = this.todos.find((t) => t.id === todoId)

      if (e.target.classList.contains("todo-checkbox")) {
        // Toggle completion status
        todo.completed = e.target.checked
        this.saveTodos()
        this.renderTodos()
      } else if (e.target.classList.contains("edit-btn")) {
        // Edit todo
        const newText = prompt("Edit task:", todo.text)
        if (newText !== null && newText.trim() !== "") {
          todo.text = newText.trim()
          this.saveTodos()
          this.renderTodos()
        }
      } else if (e.target.classList.contains("delete-btn")) {
        // Delete todo
        if (confirm("Are you sure you want to delete this task?")) {
          this.todos = this.todos.filter((t) => t.id !== todoId)
          this.saveTodos()
          this.renderTodos()
        }
      }
    })
  }

  // Render todos based on current filter
  renderTodos() {
    const todoList = document.getElementById("todo-list")
    todoList.innerHTML = ""

    // Filter todos based on current filter
    let filteredTodos = [...this.todos]
    if (this.currentFilter === "active") {
      filteredTodos = filteredTodos.filter((todo) => !todo.completed)
    } else if (this.currentFilter === "completed") {
      filteredTodos = filteredTodos.filter((todo) => todo.completed)
    }

    // Sort todos by creation date (newest first)
    filteredTodos.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt))

    if (filteredTodos.length === 0) {
      todoList.innerHTML = `<li class="todo-item" style="justify-content: center; color: var(--text-light);">No tasks found</li>`
      return
    }

    // Create todo items
    filteredTodos.forEach((todo) => {
      const todoItem = document.createElement("li")
      todoItem.classList.add("todo-item")
      if (todo.completed) {
        todoItem.classList.add("completed")
      }
      todoItem.dataset.id = todo.id

      todoItem.innerHTML = `
        <input type="checkbox" class="todo-checkbox" ${todo.completed ? "checked" : ""}>
        <span class="todo-text">${this.escapeHtml(todo.text)}</span>
        <div class="todo-actions">
          <button class="btn edit-btn">Edit</button>
          <button class="btn delete-btn">Delete</button>
        </div>
      `

      todoList.appendChild(todoItem)
    })
  }

  // Save todos to localStorage
  saveTodos() {
    localStorage.setItem("todos", JSON.stringify(this.todos))
  }

  // Initialize Schedule functionality
  initializeSchedule() {
    const scheduleForm = document.getElementById("schedule-form")
    const scheduleList = document.getElementById("schedule-list")
    const dayButtons = document.querySelectorAll(".day-btn")

    // Render initial schedule
    this.renderSchedule()

    // Add new class
    scheduleForm.addEventListener("submit", (e) => {
      e.preventDefault()

      const day = document.getElementById("class-day").value
      const name = document.getElementById("class-name").value.trim()
      const time = document.getElementById("class-time").value
      const duration = document.getElementById("class-duration").value
      const location = document.getElementById("class-location").value.trim()

      if (name && time) {
        const newClass = {
          id: Date.now(),
          day,
          name,
          time,
          duration,
          location,
        }

        this.schedule.push(newClass)
        this.saveSchedule()
        this.renderSchedule()

        // Reset form
        scheduleForm.reset()
        document.getElementById("class-day").value = this.currentDay
      }
    })

    // Filter schedule by day
    dayButtons.forEach((button) => {
      button.addEventListener("click", () => {
        dayButtons.forEach((btn) => btn.classList.remove("active"))
        button.classList.add("active")

        this.currentDay = button.dataset.day
        document.getElementById("class-day").value = this.currentDay
        this.renderSchedule()
      })
    })

    // Handle schedule actions (edit, delete)
    scheduleList.addEventListener("click", (e) => {
      const scheduleItem = e.target.closest(".schedule-item")
      if (!scheduleItem) return

      const scheduleId = Number(scheduleItem.dataset.id)
      const scheduleClass = this.schedule.find((s) => s.id === scheduleId)

      if (e.target.classList.contains("edit-btn")) {
        // Edit class
        document.getElementById("class-day").value = scheduleClass.day
        document.getElementById("class-name").value = scheduleClass.name
        document.getElementById("class-time").value = scheduleClass.time
        document.getElementById("class-duration").value = scheduleClass.duration
        document.getElementById("class-location").value = scheduleClass.location || ""

        // Remove the class from schedule
        this.schedule = this.schedule.filter((s) => s.id !== scheduleId)
        this.saveSchedule()
        this.renderSchedule()

        // Focus on the form
        document.getElementById("class-name").focus()
      } else if (e.target.classList.contains("delete-btn")) {
        // Delete class
        if (confirm("Are you sure you want to delete this class?")) {
          this.schedule = this.schedule.filter((s) => s.id !== scheduleId)
          this.saveSchedule()
          this.renderSchedule()
        }
      }
    })
  }

  // Render schedule based on current day
  renderSchedule() {
    const scheduleList = document.getElementById("schedule-list")
    scheduleList.innerHTML = ""

    // Filter schedule by current day
    const daySchedule = this.schedule.filter((item) => item.day === this.currentDay)

    // Sort by time
    daySchedule.sort((a, b) => a.time.localeCompare(b.time))

    if (daySchedule.length === 0) {
      scheduleList.innerHTML = `<div class="schedule-item" style="text-align: center; color: var(--text-light);">No classes scheduled for ${this.currentDay}</div>`
      return
    }

    // Create schedule items
    daySchedule.forEach((item) => {
      const scheduleItem = document.createElement("div")
      scheduleItem.classList.add("schedule-item")
      scheduleItem.dataset.id = item.id

      // Format time for display
      const formattedTime = this.formatTime(item.time)
      const endTime = this.calculateEndTime(item.time, item.duration)

      scheduleItem.innerHTML = `
        <div class="schedule-item-header">
          <span class="class-name">${this.escapeHtml(item.name)}</span>
          <span class="class-time">${formattedTime} - ${endTime}</span>
        </div>
        ${item.location ? `<div class="class-location">📍 ${this.escapeHtml(item.location)}</div>` : ""}
        <div class="schedule-actions">
          <button class="btn edit-btn">Edit</button>
          <button class="btn delete-btn">Delete</button>
        </div>
      `

      scheduleList.appendChild(scheduleItem)
    })
  }

  // Save schedule to localStorage
  saveSchedule() {
    localStorage.setItem("schedule", JSON.stringify(this.schedule))
  }

  // Initialize Notes functionality
  initializeNotes() {
    const notesForm = document.getElementById("notes-form")
    const notesList = document.getElementById("notes-list")

    // Render initial notes
    this.renderNotes()

    // Add new note
    notesForm.addEventListener("submit", (e) => {
      e.preventDefault()

      const title = document.getElementById("note-title").value.trim()
      const content = document.getElementById("note-content").value.trim()

      if (title && content) {
        const newNote = {
          id: Date.now(),
          title,
          content,
          createdAt: new Date().toISOString(),
        }

        this.notes.push(newNote)
        this.saveNotes()
        this.renderNotes()

        // Reset form
        notesForm.reset()
      }
    })

    // Handle note actions (edit, delete)
    notesList.addEventListener("click", (e) => {
      const noteCard = e.target.closest(".note-card")
      if (!noteCard) return

      const noteId = Number(noteCard.dataset.id)
      const note = this.notes.find((n) => n.id === noteId)

      if (e.target.classList.contains("edit-btn")) {
        // Edit note
        document.getElementById("note-title").value = note.title
        document.getElementById("note-content").value = note.content

        // Remove the note
        this.notes = this.notes.filter((n) => n.id !== noteId)
        this.saveNotes()
        this.renderNotes()

        // Focus on the form
        document.getElementById("note-title").focus()
      } else if (e.target.classList.contains("delete-btn")) {
        // Delete note
        if (confirm("Are you sure you want to delete this note?")) {
          this.notes = this.notes.filter((n) => n.id !== noteId)
          this.saveNotes()
          this.renderNotes()
        }
      }
    })
  }

  // Render notes
  renderNotes() {
    const notesList = document.getElementById("notes-list")
    notesList.innerHTML = ""

    // Sort notes by creation date (newest first)
    const sortedNotes = [...this.notes].sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt))

    if (sortedNotes.length === 0) {
      notesList.innerHTML = `<div class="note-card" style="text-align: center; color: var(--text-light);">No notes yet</div>`
      return
    }

    // Create note cards
    sortedNotes.forEach((note) => {
      const noteCard = document.createElement("div")
      noteCard.classList.add("note-card")
      noteCard.dataset.id = note.id

      // Format date for display
      const formattedDate = new Date(note.createdAt).toLocaleDateString("en-US", {
        year: "numeric",
        month: "short",
        day: "numeric",
      })

      noteCard.innerHTML = `
        <div class="note-title">${this.escapeHtml(note.title)}</div>
        <div class="note-content">${this.escapeHtml(note.content)}</div>
        <div class="note-date">${formattedDate}</div>
        <div class="note-actions">
          <button class="btn edit-btn">Edit</button>
          <button class="btn delete-btn">Delete</button>
        </div>
      `

      notesList.appendChild(noteCard)
    })
  }

  // Save notes to localStorage
  saveNotes() {
    localStorage.setItem("notes", JSON.stringify(this.notes))
  }

  // Helper function to format time (24h to 12h)
  formatTime(time24h) {
    const [hours, minutes] = time24h.split(":")
    const period = hours >= 12 ? "PM" : "AM"
    const hours12 = hours % 12 || 12
    return `${hours12}:${minutes} ${period}`
  }

  // Helper function to calculate end time
  calculateEndTime(startTime, durationMinutes) {
    const [hours, minutes] = startTime.split(":").map(Number)

    // Convert to total minutes, add duration, then convert back
    const totalMinutes = hours * 60 + minutes + Number.parseInt(durationMinutes)
    const endHours = Math.floor(totalMinutes / 60) % 24
    const endMinutes = totalMinutes % 60

    // Format end time
    const period = endHours >= 12 ? "PM" : "AM"
    const hours12 = endHours % 12 || 12
    return `${hours12}:${endMinutes.toString().padStart(2, "0")} ${period}`
  }

  // Helper function to escape HTML to prevent XSS
  escapeHtml(text) {
    const div = document.createElement("div")
    div.textContent = text
    return div.innerHTML
  }

  // Simulate fetching weather data (async/await example)
  async fetchWeatherData() {
    try {
      // This is a simulation - in a real app, you would call an actual API
      await new Promise((resolve) => setTimeout(resolve, 1000))
      return {
        temperature: Math.floor(Math.random() * 30) + 10,
        condition: ["Sunny", "Cloudy", "Rainy", "Snowy"][Math.floor(Math.random() * 4)],
      }
    } catch (error) {
      console.error("Error fetching weather data:", error)
      return null
    }
  }
}

// Initialize the dashboard when the DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
  const app = new Dashboard()

  // Example of using async/await with the simulated weather API
  const fetchWeather = async () => {
    const weatherData = await app.fetchWeatherData()
    if (weatherData) {
      console.log(`Weather: ${weatherData.temperature}°C, ${weatherData.condition}`)
      // In a real app, you would update the UI with this data
    }
  }

  fetchWeather()
})
