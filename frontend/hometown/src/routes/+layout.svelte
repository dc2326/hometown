<style>
    .page-stuff {
        position: relative;
        min-height: 100vh;
    }

    .container {
        padding-bottom: 5rem;
    }
</style>

<script>
    import Navbar from '$lib/Navbar.svelte';
    import Footer from '$lib/Footer.svelte';
</script>

<div class="page-stuff">
    <Navbar/>

    <div class="container">
        <slot />
    </div>
    
    <Footer/>    
</div>