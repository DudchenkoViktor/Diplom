document.addEventListener('DOMContentLoaded', function () {
    // Получаем все кнопки переключения видимости пароля
    const togglePasswordButtons = document.querySelectorAll('.toggle-password');

    togglePasswordButtons.forEach(button => {
        // Получаем связанное поле пароля
        const passwordField = document.querySelector(button.getAttribute('data-target'));

        if (passwordField) {
            // Добавляем обработчик клика для кнопки
            button.addEventListener('click', function () {
                // Переключаем тип поля пароля
                const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
                passwordField.setAttribute('type', type);

                // Переключаем иконку
                const icon = button.querySelector('.material-icons');
                icon.textContent = type === 'password' ? 'visibility' : 'visibility_off';
            });
        }
    });

    // Копирование пароля из password1 в password2
    const password1 = document.getElementById('id_password1');
    const password2 = document.getElementById('id_password2');

    if (password1 && password2) {
        password1.addEventListener('input', function () {
            password2.value = password1.value;
        });
    }
});


document.getElementById('id_image').addEventListener('change', function (e) {
    const file = e.target.files[0];
    if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
    document.querySelector('.profile-image').src = e.target.result;
}
    reader.readAsDataURL(file);
}
});


