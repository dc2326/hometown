<style>
    .info-container {
        border-radius: 18px;
        margin: 2rem auto;
        justify-self: center;
        justify-content: center;
        box-shadow: 0 4px 12px rgba(43, 43, 43, 0.1);
        border: 1px solid rgba(45, 90, 39, 0.1);
    }

    .h1-custom {
        color: darkgreen;
    }

    .title {
        margin-top: 2rem;
        margin-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
        padding-bottom: 2rem;
        justify-items: center;
        border-bottom: 2px solid gray;
        margin-left: 5rem;
        margin-right: 5rem;
    }

    .textblock {
        padding-left: 2rem;
        padding-right: 2rem;
    }

    .subtitle {
        margin-top: 1rem;
        margin-bottom: 0;
        padding-left: 2rem;
        padding-right: 2rem;
        justify-self: center;
    }

    .showcase {
        display: flex;
        flex-grow: 1;
    }

    .card {
        justify-items: center;
    }

    .profile {
        height: 400px;
        padding: 1rem;
    }

    .description {
        justify-items: center;
    }

</style>

<div class="info-container">
    <div class="title">
        <h1 class="h1 h1-custom">About Us</h1>
    </div>
    <div class="content">
        <section>
            <div class="subtitle">
                <h1 class="h2 h1-custom">Our Mission</h1>
            </div>
            <div class="textblock">
                <p> 
                    We aim to improve the interpersonal relationships within members of a community and the transparency of
                    your local government. From members of the town council to your neighbor across the street, we believe that 
                    as members of your hometown, everyone deserves to experience the convenience and inclusivity that being part 
                    of a community brings you. HomeTown makes it easy to create and join community clubs, see what is going on in 
                    your neighborhood, meet new people, pay taxes and see how they are being used.
                </p>
            </div>
        </section>
        <section>
            <div class="subtitle">
                <h1 class="h2 h1-custom">Who we are</h1>
            </div>
            <div class="showcase">
                <div class="card info-container">
                    <img src="dak.jpeg" alt="Dak Cheung Cheng" class="profile">
                    <div class="description">
                        <div class="name-text">
                            <h3 class="h3">
                                Dak Cheung Cheng
                            </h3>
                        </div>
                        <div class="job-text">
                            <h6 class="h6">
                                Lead Software Engineer
                            </h6>
                        </div>
                    </div>
                </div>
                <div class="card info-container">
                    <img src="jack.jpeg" alt="Jack Hasker" class="profile">
                    <div class="description">
                        <div class="name-text">
                            <h3 class="h3">
                                Jack Hasker
                            </h3>
                        </div>
                        <div class="job-text">
                            <h6 class="h6">
                                Market and Growth Manager
                            </h6>
                        </div>
                    </div>
                </div>
                <div class="card info-container">
                    <img src="john.jpeg" alt="John Giess" class="profile">
                    <div class="description">
                        <div class="name-text">
                            <h3 class="h3">
                                John Giess
                            </h3>
                        </div>
                        <div class="job-text">
                            <h6 class="h6">
                                Lead Product Designer
                            </h6>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</div>