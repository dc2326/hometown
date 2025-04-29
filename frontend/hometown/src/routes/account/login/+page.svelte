<style>
    .register {
        justify-items: center;
        justify-self: center;
        border-radius: 18px;
        box-shadow: 0 4px 16px rgba(44,62,80,0.10);
        padding: 2.5rem 2rem 2rem 2rem;
        margin-bottom: 4rem;
        margin-top: 4rem;
        width:100vh;
    }

    .information {
        max-width: 300px;
        padding: 10px;
    }

    .inputinfo {
        justify-content: center;
        display: flex;
        flex-direction: column;
    }

    .welcome {
        margin: 5%;
        justify-content: center;
        justify-items: center;
    }

</style>

<div class="register">
    <div class="welcome">
        <h1 class="h1">Welcome Back</h1>
        <h2 class="text-muted">We missed you</h2>
    </div>
    <form class="information">
        <label class="inputinfo">
            <span class="user-text">Username</span>
            <input type="text" class="input" required>
        </label>
        <label class="inputinfo">
            <span class="pass-text">Password</span>
            <input type="password" class="input" required>
        </label>
        <input type="submit" class="btn btn-dark" value="Log In">
    </form>
</div>