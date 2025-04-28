<style>
    .navbar {
        transition: top 0.3s;
        position: static;
        width: 100%;
        background-color: white;
        top: 0;
        left: 0;
        z-index: 999;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .nav-link {
        position: relative;
        display: inline-block;
        overflow: hidden;
    }
    
    .nav-link::after {
        content: "";
        position: absolute;
        left: 0;
        bottom: 0;
        height: 2px;
        width: 0;
        background-color: currentColor; /* match text color */
        transition: width 0.3s ease;
    }
    
    .nav-link:hover::after {
        width: 100%;
    }

    .custom {
        background-color: #2f2ff4;
    }

    .custom:hover {
        background-color: #7f2df9;
    }

</style>

<script>
    import logo from '$lib/logo.png';
</script>

<header>
    <nav class="navbar-expand-lg navbar-light bg-light navbar">
        <div class="container-fluid">
            <div class="col-lg-3 d-flex justify-content-start px-5">
                <a href="/" aria-label="HomeTown">
                    <img src={logo} alt="HomeTown logo" height=75px>
                </a>
            </div>
            <div class="navbar-collapse collapse d-flex justify-content-center col-lg-6" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item ms-3 me-3">
                        <a class="nav-link" href="/community">Community</a>
                    </li>
                    <li class="nav-item ms-3 me-3">
                        <a class="nav-link" href="/news">News</a>
                    </li>
                    <li class="nav-item ms-3 me-3">
                        <a class="nav-link" href="/council">Council</a>
                    </li>
                </ul>
            </div>
            <div class="col-lg-3 d-flex justify-content-end">
                <button class="px-3 btn btn-primary custom">Sign Up</button>
                <button class="px-3 ms-1 me-5 btn btn-secondary">Login</button>
            </div>
        </div>
    </nav>
</header>