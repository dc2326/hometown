<script>
    import Navbar from '$lib/Navbar.svelte';
    import Footer from '$lib/Footer.svelte';
</script>

<Navbar/>

<div class="container">
    <slot />
</div>

<Footer />
