<script setup lang="ts">
import { isEqual } from 'lodash-es';
import type { TradeLocationData } from '@/types/history/trade/location';

const props = withDefaults(
  defineProps<{
    value?: string;
    items?: string[];
    excludes?: string[];
    attach?: string;
  }>(),
  { value: '', items: () => [], excludes: () => [], attach: undefined },
);

const emit = defineEmits<{
  (e: 'input', value: string): void;
}>();

const model = useSimpleVModel(props, emit);
const rootAttrs = useAttrs();

const { items, excludes } = toRefs(props);

const { tradeLocations } = useLocations();

const locations = computed<TradeLocationData[]>(() => {
  const itemsVal = get(items);
  const excludesVal = get(excludes);

  return get(tradeLocations).filter((item) => {
    const included
      = itemsVal && itemsVal.length > 0
        ? itemsVal.includes(item.identifier)
        : true;

    const excluded
      = excludesVal && excludesVal.length > 0
        ? excludesVal.includes(item.identifier)
        : false;

    return included && !excluded;
  });
});

watch([locations, model], ([locations, value], [prevLocations, prevValue]) => {
  if (isEqual(locations, prevLocations) && value === prevValue)
    return;

  if (!locations.some(item => item.identifier === value))
    set(model, '');
});
</script>

<template>
  <RuiAutoComplete
    v-model="model"
    variant="outlined"
    data-cy="location-input"
    :options="locations"
    key-attr="identifier"
    text-attr="name"
    :item-height="52"
    auto-select-first
    v-bind="rootAttrs"
    v-on="
      // eslint-disable-next-line vue/no-deprecated-dollar-listeners-api
      $listeners
    "
  >
    <template #item="{ item }">
      <LocationIcon
        :id="`balance-location__${item.identifier}`"
        class="!justify-start"
        horizontal
        :item="item.identifier"
      />
    </template>
    <template #selection="{ item }">
      <LocationIcon
        class="!justify-start pr-2"
        horizontal
        :item="item.identifier"
      />
    </template>
  </RuiAutoComplete>
</template>
