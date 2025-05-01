document.getElementById('password').addEventListener('input', function() {
    const password = this.value;
    fetch('/check_password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ password: password })
    })
    .then(response => response.json())
    .then(data => {
        const strengthBar = document.getElementById('strength-bar');
        const feedback = document.getElementById('feedback');
        strengthBar.style.backgroundColor = data.color;
        feedback.textContent = data.message;
    });
});
document.getElementById('togglePassword').addEventListener('click', function () {
    const password = document.getElementById('password');
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    this.classList.toggle('fa-eye');
    this.classList.toggle('fa-eye-slash');
});
