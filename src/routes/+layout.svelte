<script lang="ts">
	import '../lib/styles/global.css';
	import Navigation from '$lib/components/Navigation.svelte';
	import { page } from '$app/stores';
	
	$: pageTitle = $page.data?.title || 'home';
</script>

<div class="main-body pure-g">
	<Navigation />
	<div id={pageTitle} class="pure-u-4-5 main-content">
		<slot />
	</div>
</div>

