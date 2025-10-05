<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
	import Navbar from '$lib/components/Navbar.svelte';
	import Footbar from '$lib/components/footbar.svelte';

	let { children } = $props();
</script>


<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<header>
	<Navbar/>
</header>
{@render children?.()}
<Footbar/>