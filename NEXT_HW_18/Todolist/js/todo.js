document.addEventListener("DOMContentLoaded", function() {
  const todoForm = document.getElementById("todo-form");
  const todoList = document.getElementById("todo-list");
  const todoInput = document.getElementById("content");

  loadTodos();

  todoForm.addEventListener("submit", function(event) {
      event.preventDefault();
      
      const todoContent = todoInput.value.trim();
      if (todoContent === "") return;

      const newTodo = {
          id: Date.now(),
          content: todoContent,
          completed: false
      };

      saveTodoToLocalStorage(newTodo);

      addTodoToDOM(newTodo);
      todoInput.value = "";
  });

  function loadTodos() {
      const todosString = localStorage.getItem("todos");
      const todos = todosString ? JSON.parse(todosString) : [];
      todos.forEach(addTodoToDOM);
  }

  function saveTodoToLocalStorage(todo) {
      const todosString = localStorage.getItem("todos");
      const todos = todosString ? JSON.parse(todosString) : [];
      todos.push(todo);
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
      const todosString = localStorage.getItem("todos");
      const todos = todosString ? JSON.parse(todosString) : [];
      const updatedTodos = todos.filter(todo => todo.id !== id);
      localStorage.setItem("todos", JSON.stringify(updatedTodos));
  }
});