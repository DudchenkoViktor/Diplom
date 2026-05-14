function updateDropdown(displayElementId, value, hiddenInputId) {
    // Получаем элемент для отображения текста
    const displayElement = document.getElementById(displayElementId);

    const sort_name = {
        'Z-A': '-last_name',
        'A-Z': 'last_name',
        'By experience': 'experience',
        'By age': 'age'
    };

    // Обновляем текст элемента отображения в зависимости от типа
    if (displayElementId === 'expId') {
        displayElement.innerText = value + ' studying';
    } else if (displayElementId === 'sortId') {
        displayElement.innerText = value;
    } else {
        displayElement.innerText = value;
    }

    // Обновляем значение скрытого поля
    const hiddenInput = document.getElementById(hiddenInputId);
    if (hiddenInputId === 'sortInput') {
         hiddenInput.value = sort_name[value];
    } else {
          hiddenInput.value = value; // Устанавливаем значение скрытого поля
    }
}


