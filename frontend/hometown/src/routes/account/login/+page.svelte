<script>
    let email = '';
    let password = '';
    let rememberMe = false;

    function handleLogin() {
        // Here we would typically send the data to a backend
        console.log('Login attempt:', { email, password, rememberMe });
        // For now, we'll just show an alert
        alert('Login successful!');
    }
</script>

<style>
    :root {
        --primary-green: #2d5a27;
        --light-green: #3a7a33;
        --accent-gold: #d4af37;
        --background: #f5f5f0;
        --card-bg: #fff;
        --card-shadow: 0 4px 12px rgba(43, 43, 43, 0.1);
        --border-radius: 12px;
        --text-main: #222;
        --text-muted: #666;
    }

    .login-container {
        max-width: 400px;
        margin: 2rem auto;
        padding: 0 1rem;
    }

    .login-card {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        padding: 2rem;
        border: 1px solid rgba(45, 90, 39, 0.1);
    }

    .login-title {
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

    .remember-me {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
    }

    .remember-me input {
        margin-right: 0.5rem;
    }

    .login-btn {
        background: var(--accent-gold);
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

    .login-btn:hover {
        background: #e0c060;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.2);
    }

    .signup-link {
        text-align: center;
        margin-top: 1.5rem;
        color: var(--text-muted);
    }

    .signup-link a {
        color: var(--primary-green);
        text-decoration: none;
        font-weight: 600;
    }

    .signup-link a:hover {
        text-decoration: underline;
    }
</style>

<div class="login-container">
    <div class="login-card">
        <h1 class="login-title">Welcome Back</h1>
        
        <form on:submit|preventDefault={handleLogin}>
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
                    placeholder="Enter your password"
                />
            </div>

            <div class="remember-me">
                <input type="checkbox" id="remember" bind:checked={rememberMe} />
                <label for="remember">Remember me</label>
            </div>

            <button type="submit" class="login-btn">Login</button>
        </form>

        <div class="signup-link">
            Don't have an account? <a href="/account/register">Sign up</a>
        </div>
    </div>
</div> 