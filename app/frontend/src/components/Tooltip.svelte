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

	const OFFSET = 2.5;

	function onParentMouseEnter() {
		visible = true;
	}

	function onParentMouseLeave() {
		visible = false;
	}

	function onParentMouseMove(e: MouseEvent) {
		const rect = tooltipEl?.parentElement.getBoundingClientRect();
		const tw = tooltipEl?.offsetWidth ?? 0;
		const th = tooltipEl?.offsetHeight ?? 0;
		let nx = e.clientX - rect.left;
		let ny = e.clientY - rect.top;
		switch(position) {
			case 'top':
				ny -= th + OFFSET;
				nx -= tw / 2;
				break;
			case 'bottom':
				ny += OFFSET;
				nx -= tw / 2;
				break;
			case 'left':
				nx -= tw + OFFSET;
				ny -= th / 2 + OFFSET;
				break;
			case 'right':
				nx += OFFSET;
				ny -= th / 2 + OFFSET;
				break;
			case 'top-left':
				ny -= th + OFFSET;
				nx -= tw + OFFSET;
				break;
			case 'top-right':
				ny -= th + OFFSET;
				nx += OFFSET;
				break;
			case 'bottom-left':
				ny += OFFSET;
				nx -= tw + OFFSET;
				break;
			case 'bottom-right':
				ny += OFFSET;
				nx += OFFSET;
				break;
		}

		// Clamp to viewport bounds (coordinates are relative to parent element)
		const minX = -rect.left;
		const minY = -rect.top;
		const maxX = window.innerWidth - rect.left - tw;
		const maxY = window.innerHeight - rect.top - th;
		x = Math.min(Math.max(nx, minX), maxX);
		y = Math.min(Math.max(ny, minY), maxY);
	}

	onMount(() => {
		const parent = tooltipEl?.parentElement;
		if (!parent) return;

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