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
