document.querySelectorAll("[data-todo-remove]").forEach((e) =>
  e.addEventListener("click", (e) => {
    if (!confirm("Tem certeza que deseja remover esta tarefa?")) return false;

    const el = e.target;
    const id = el.dataset.todoRemove;
    const parent = el.closest("li");

    fetch(`/${id}`, {
      method: "DELETE",
    }).then(() => {
      parent.remove();
    });
  })
);

document.querySelectorAll("[data-todo-toggle-status]").forEach((e) =>
  e.addEventListener("click", (e) => {
    const el = e.target;
    const id = el.dataset.todoToggleStatus;
    const label = el.parentElement.querySelector("label");

    label.classList.toggle("closed");

    fetch(`/${id}/toggleStatus`, {
      method: "POST",
    });
  })
);
