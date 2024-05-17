document.addEventListener("DOMContentLoaded", function() {
  const todoForm = document.getElementById("todo-form");
  const todoList = document.getElementById("todo-list");
  const todoInput = document.getElementById("content");

  // Load existing todos from localStorage
  loadTodos();

  todoForm.addEventListener("submit", function(event) {
      event.preventDefault();
      
      const todoContent = todoInput.value.trim();
      if (todoContent === "") return;

      // Create a new todo object
      const newTodo = {
          id: Date.now(),
          content: todoContent,
          completed: false
      };

      // Save to localStorage
      saveTodoToLocalStorage(newTodo);

      // Add to the DOM
      addTodoToDOM(newTodo);

      // Clear the input field
      todoInput.value = "";
  });

  function loadTodos() {
      // 로컬 스토리지에서 할 일 목록 가져오기
      const todosString = localStorage.getItem("todos");
      const todos = todosString ? JSON.parse(todosString) : [];
      todos.forEach(addTodoToDOM);
  }

  function saveTodoToLocalStorage(todo) {
      // 로컬 스토리지에서 기존 할 일 목록 가져오기
      const todosString = localStorage.getItem("todos");
      const todos = todosString ? JSON.parse(todosString) : [];
      todos.push(todo);
      // 업데이트된 할 일 목록을 JSON 문자열로 변환하여 저장
      localStorage.setItem("todos", JSON.stringify(todos));
  }

  function addTodoToDOM(todo) {
      const todoItem = document.createElement("li");
      todoItem.innerText = todo.content;
      todoItem.setAttribute("data-id", todo.id);

      const deleteButton = document.createElement("button");
      deleteButton.innerText = "삭제";
      deleteButton.onclick = function() {
          deleteTodoFromLocalStorage(todo.id);
          todoItem.remove();
      };

      todoItem.appendChild(deleteButton);
      todoList.appendChild(todoItem);
  }

  function deleteTodoFromLocalStorage(id) {
      // 로컬 스토리지에서 기존 할 일 목록 가져오기
      const todosString = localStorage.getItem("todos");
      const todos = todosString ? JSON.parse(todosString) : [];
      // 해당 id를 가진 할 일을 목록에서 제거
      const updatedTodos = todos.filter(todo => todo.id !== id);
      // 업데이트된 할 일 목록을 JSON 문자열로 변환하여 저장
      localStorage.setItem("todos", JSON.stringify(updatedTodos));
  }
});