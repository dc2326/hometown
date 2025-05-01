<style>
    .navbar {
        padding: 1rem 0;
        background: #fff;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }

    .nav-link {
        font-size: 1.2rem;
        font-weight: 600;
        color: var(--primary-green);
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        transition: all 0.3s ease;
        text-decoration: none;
    }

    .nav-link:hover {
        background: rgba(45, 90, 39, 0.1);
        color: var(--primary-green);
        transform: translateY(-2px);
    }

    .btn-primary.custom {
        background: var(--primary-green);
        color: white;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        transition: all 0.3s ease;
    }

    .btn-primary.custom:hover {
        background: var(--light-green);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(45, 90, 39, 0.2);
    }

    .btn-secondary {
        background: var(--accent-gold);
        color: white;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        transition: all 0.3s ease;
    }

    .btn-secondary:hover {
        background: #e0c060;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.2);
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
                        <a class="nav-link" href="/services">Services</a>
                    </li>
                </ul>
            </div>
            <div class="col-lg-3 d-flex justify-content-end">
                <a href="/account/register" class="px-3 btn btn-primary custom">Sign Up</a>
                <a href="/account/login" class="px-3 ms-1 me-5 btn btn-secondary">Login</a>
            </div>
        </div>
    </nav>
</header>