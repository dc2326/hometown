<style>
    .bannerx {
        background-color: red;
        border-radius: 10px;
        display: flex;
        margin: 0.25em;
        width: 100%vp;
    }

    .content {
        display: flex;
    }

    .messages {
        background-color: rgb(245, 245, 255);
        border-radius: 10px;
        display: flex;
        flex-direction: row;
        margin: 0.25em;
        justify-content: center;
        height: 80vh;
    }

    .info {
        display: block;
        justify-items: center;
    }

    .public {
        width: 33%;
    }

    .private {
        flex-grow: 1;
    }

    .hidden {
        display: none;
    }

</style>

<div class="bannerx px-3">
    <p>Notification: Blah blah blah</p>
</div>
<div class="content">
    <div class="messages private">
        <div class="info">
            <h1>Bulletin Board</h1>
            <p>Sign in to see your personalized notifications from things you care about.</p>
            <!-- <Bulletin /> -->
        </div>
    </div>
    <div class="messages public">
        <div class="info">
            <!-- <PublicNews /> -->
            <h1>Public Notice</h1>
            <ul>
                <li>No news.</li>
            </ul>
        </div>
    </div>
</div>