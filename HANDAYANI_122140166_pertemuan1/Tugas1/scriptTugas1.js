const taskList = document.getElementById("taskList");
const taskInput = document.getElementById("taskInput");
let currentColorIndex = 0;

document.getElementById("Tambah").addEventListener("click", function () {
    const text = taskInput.value.trim();
    if (text !== "") {
        renderTask(text);
        taskInput.value = "";
        saveTasks();
    }
});

function renderTask(text, completed = false) {
    let li = document.createElement("li");
    li.classList.add("p-3", "rounded", "task-item", "flex", "justify-between", "items-center", "bg-gray-100", "border", "border-gray-700");

    let span = document.createElement("span");
    span.textContent = text;
    if (completed) span.classList.add("completed");

    let buttonContainer = document.createElement("div");
    buttonContainer.classList.add("flex", "gap-5");

    let deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Hapus";
    deleteBtn.classList.add("text-red-500", "hover:text-red-700");
    deleteBtn.addEventListener("click", function () {
        li.remove();
        saveTasks(); 
    });

    let checkBtn = document.createElement("button");
    checkBtn.textContent = "Done";
    checkBtn.classList.add("text-green-500", "hover:text-green-700");
    checkBtn.addEventListener("click", function () {
        span.classList.toggle("completed");
        saveTasks(); 
    });

    buttonContainer.appendChild(deleteBtn);
    buttonContainer.appendChild(checkBtn);

    li.appendChild(span);
    li.appendChild(buttonContainer);
    taskList.appendChild(li);
}

function saveTasks() {
    let tasks = [];
    document.querySelectorAll("#taskList li").forEach(li => {
        tasks.push({
            text: li.querySelector("span").textContent,
            completed: li.querySelector("span").classList.contains("completed")
        });
    });
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

document.getElementById("HapusSemua").addEventListener("click", function () {
    taskList.innerHTML = "";
    localStorage.removeItem("tasks"); // Hapus data dari localStorage
});

document.getElementById("HapusPilih").addEventListener("click", function () {
    document.querySelectorAll(".completed").forEach(task => task.parentElement.remove());
    saveTasks(); // Simpan perubahan setelah menghapus item yang selesai
});

document.getElementById("Urutkan").addEventListener("click", function () {
    let items = [...taskList.children];
    items.sort((a, b) => a.textContent.localeCompare(b.textContent));
    taskList.innerHTML = "";
    items.forEach(item => taskList.appendChild(item));
    saveTasks(); // Simpan perubahan setelah mengurutkan
});

document.getElementById("Ganti").addEventListener("click", function () {
    document.getElementById("taskList").classList.toggle("bg-blue-100");
});

// Fungsi untuk memuat tugas dari localStorage saat halaman dimuat
function loadTasks() {
    let savedTasks = localStorage.getItem("tasks");
    if (savedTasks) {
        JSON.parse(savedTasks).forEach(task => {
            renderTask(task.text, task.completed);
        });
    }
}

// Memuat daftar tugas saat halaman pertama kali dibuka
document.addEventListener("DOMContentLoaded", loadTasks);
