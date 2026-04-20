<style lang="scss">
	.tooltip {
		position: absolute;
		background-color: #221F10;
		color: #EECD2B;
		border: 1px solid rgba(238, 205, 43, .4);
		border-radius: 4px;
		padding: 4px 8px;
		font-size: 12px;
		pointer-events: none;
		white-space: nowrap;
		opacity: 0;
		transition: opacity 0.15s ease;
		z-index: 9999;

		&--visible {
			opacity: 1;
		}
	}
</style>

<div
	class="tooltip"
	class:tooltip--visible={visible}
	style="left: {x}px; top: {y}px;"
	bind:this={tooltipEl}
>
	{text}
</div>

<script lang="ts">
	import { onMount } from 'svelte';

	type TooltipProps = {
		text: string;
		position?: "top" | "bottom" | "left" | "right" | "top-left" | "top-right" | "bottom-left" | "bottom-right";
	}

	const { text, position = 'bottom-right' }: TooltipProps = $props();

	let visible = $state(false);
	let x = $state(0);
	let y = $state(0);
	let tooltipEl = $state<HTMLDivElement | null>(null);
	let rect: DOMRect = null;

	const OFFSET = 2.5;

	function onParentMouseEnter() {
		visible = true;
	}

	function onParentMouseLeave() {
		visible = false;
	}

	function onParentMouseMove(e: MouseEvent) {
		x = e.pageX - rect.left;
		y = e.pageY - rect.top;
		switch(position) {
			case 'top':
				y -= tooltipEl?.offsetHeight + OFFSET;
				x -= tooltipEl?.offsetWidth / 2;
				break;
			case 'bottom':
				y += OFFSET;
				x -= tooltipEl?.offsetWidth / 2;
				break;
			case 'left':
				x -= tooltipEl?.offsetWidth + OFFSET;
				y -= tooltipEl?.offsetHeight / 2 + OFFSET;
				break;
			case 'right':
				x += OFFSET;
				y -= tooltipEl?.offsetHeight / 2 + OFFSET;
				break;
			case 'top-left':
				y -= tooltipEl?.offsetHeight + OFFSET;
				x -= tooltipEl?.offsetWidth + OFFSET;
				break;
			case 'top-right':
				y -= tooltipEl?.offsetHeight + OFFSET;
				x += OFFSET;
				break;
			case 'bottom-left':
				y += OFFSET;
				x -= tooltipEl?.offsetWidth + OFFSET;
				break;
			case 'bottom-right':
				y += OFFSET;
				x += OFFSET;
				break;
		}
	}

	onMount(() => {
		const parent = tooltipEl?.parentElement;
		if (!parent) return;
		rect = parent.getBoundingClientRect();

		parent.style.position = 'relative';
		parent.addEventListener('mouseenter', onParentMouseEnter);
		parent.addEventListener('mouseleave', onParentMouseLeave);
		parent.addEventListener('mousemove', onParentMouseMove);

		return () => {
			parent.removeEventListener('mouseenter', onParentMouseEnter);
			parent.removeEventListener('mouseleave', onParentMouseLeave);
			parent.removeEventListener('mousemove', onParentMouseMove);
		};
	});
</script>