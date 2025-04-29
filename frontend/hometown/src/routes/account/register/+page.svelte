<script>
    let firstName = '';
    let lastName = '';
    let email = '';
    let password = '';
    let confirmPassword = '';
    let agreeToTerms = false;

    function handleSignup() {
        if (password !== confirmPassword) {
            alert('Passwords do not match!');
            return;
        }
        // Here we would typically send the data to a backend
        console.log('Signup attempt:', { firstName, lastName, email, password, agreeToTerms });
        // For now, we'll just show an alert
        alert('Signup successful!');
    }
</script>

<style>
    :root {
        --primary-green: #2d5a27;
        --light-green: #3a7a33;
        --card-bg: #fff;
        --card-shadow: 0 4px 12px rgba(43, 43, 43, 0.1);
        --border-radius: 12px;
        --text-main: #2d2d2d;
        --text-muted: #666;
    }

    .signup-container {
        max-width: 400px;
        margin: 2rem auto;
        padding: 0 1rem;
    }

    .signup-card {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        padding: 2rem;
        border: 1px solid rgba(45, 90, 39, 0.1);
    }

    .signup-title {
        color: var(--primary-green);
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 2rem;
        text-align: center;
    }

    .form-group {
        margin-bottom: 1.5rem;
    }

    .form-label {
        display: block;
        color: var(--text-main);
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .form-input {
        width: 100%;
        padding: 0.75rem 1rem;
        border-radius: var(--border-radius);
        border: 1px solid rgba(45, 90, 39, 0.2);
        font-size: 1rem;
        transition: all 0.3s;
    }

    .form-input:focus {
        outline: none;
        border-color: var(--primary-green);
        box-shadow: 0 0 0 2px rgba(45, 90, 39, 0.1);
    }

    .name-fields {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
    }

    .terms {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
    }

    .terms input {
        margin-right: 0.5rem;
    }

    .terms label {
        font-size: 0.9rem;
        color: var(--text-muted);
    }

    .terms a {
        color: var(--primary-green);
        text-decoration: none;
    }

    .terms a:hover {
        text-decoration: underline;
    }

    .signup-btn {
        background: linear-gradient(90deg, var(--primary-green), var(--light-green));
        color: #fff;
        border: none;
        border-radius: var(--border-radius);
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        width: 100%;
        transition: all 0.3s;
    }

    .signup-btn:hover {
        background: linear-gradient(90deg, var(--light-green), var(--primary-green));
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(45, 90, 39, 0.2);
    }

    .login-link {
        text-align: center;
        margin-top: 1.5rem;
        color: var(--text-muted);
    }

    .login-link a {
        color: var(--primary-green);
        text-decoration: none;
        font-weight: 600;
    }

    .login-link a:hover {
        text-decoration: underline;
    }
</style>

<div class="signup-container">
    <div class="signup-card">
        <h1 class="signup-title">Create Account</h1>
        
        <form on:submit|preventDefault={handleSignup}>
            <div class="name-fields">
                <div class="form-group">
                    <label class="form-label" for="firstName">First Name</label>
                    <input
                        class="form-input"
                        type="text"
                        id="firstName"
                        bind:value={firstName}
                        required
                        placeholder="First name"
                    />
                </div>

                <div class="form-group">
                    <label class="form-label" for="lastName">Last Name</label>
                    <input
                        class="form-input"
                        type="text"
                        id="lastName"
                        bind:value={lastName}
                        required
                        placeholder="Last name"
                    />
                </div>
            </div>

            <div class="form-group">
                <label class="form-label" for="email">Email</label>
                <input
                    class="form-input"
                    type="email"
                    id="email"
                    bind:value={email}
                    required
                    placeholder="Enter your email"
                />
            </div>

            <div class="form-group">
                <label class="form-label" for="password">Password</label>
                <input
                    class="form-input"
                    type="password"
                    id="password"
                    bind:value={password}
                    required
                    placeholder="Create a password"
                />
            </div>

            <div class="form-group">
                <label class="form-label" for="confirmPassword">Confirm Password</label>
                <input
                    class="form-input"
                    type="password"
                    id="confirmPassword"
                    bind:value={confirmPassword}
                    required
                    placeholder="Confirm your password"
                />
            </div>

            <button type="submit" class="signup-btn">Create Account</button>
        </form>

        <div class="login-link">
            Already have an account? <a href="/account/login">Log in</a>
        </div>
    </div>
</div> 