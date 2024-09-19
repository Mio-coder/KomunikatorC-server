document.addEventListener('DOMContentLoaded', () => {
    const loginForm: HTMLFormElement = document.getElementById('loginForm') as HTMLFormElement;

    if (loginForm) {
        loginForm.addEventListener('submit', (event) => {
            event.preventDefault();
            // Add your form submission logic here
            console.log('Form submitted');
        });
    }
});