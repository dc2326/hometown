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
        justify-content: center;

    }

    .welcome {
        margin: 5%;
        justify-content: center;
        justify-items: center;
    }

</style>

<div class="register">
    <div class="welcome">
        <h1 class="h1">Welcome to your Community</h1>
        <h2 class="text-muted">We know you will like it here</h2>
    </div>
    <form class="information">
        <label for="user">Username:</label>
        <input type="text" id="user" name="user" required><br><br>
        <label for="pass">Password:</label>
        <input type="password" id="pass" name="pass" required><br><br>
        <label for="pass">Re-Enter Password:</label>
        <input type="password" id="pass" name="pass" required><br><br>
        <input type="submit" value="Register">
    </form>
</div>