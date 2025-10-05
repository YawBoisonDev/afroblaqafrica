<script lang="ts">
import child_birthday from '$lib/assets/portraits/L_child_birthday.jpg'
import kevin from '$lib/assets/portraits/L_kevin .jpg'
import lady from '$lib/assets/portraits/L_lady.jpg'
import sammy from '$lib/assets/portraits/L_sammy.jpg'
import sydney from '$lib/assets/portraits/L_sydney.jpg'
import wed from '$lib/assets/portraits/L_wed.jpg'
import adjo from '$lib/assets/portraits/P_adjo.jpg'
import blaqkhalif from '$lib/assets/portraits/P_blaq .jpg'
import child from '$lib/assets/portraits/P_child.jpg'
import eyiram1 from '$lib/assets/portraits/P_eyiram.jpg'
import eyiram2 from '$lib/assets/portraits/P_eyiram2.jpg'
import ladywed from '$lib/assets/portraits/P_ladywed.jpg'
import prime1 from '$lib/assets/portraits/P_prime.jpg'
import prime2 from '$lib/assets/portraits/P_prime1.jpg'
import wedguy from '$lib/assets/portraits/P_wedguy.jpg'
import yaw from '$lib/assets/portraits/P_yaw.jpg'

const Portraits = [
    child_birthday, kevin, lady, sammy,sydney,wed, adjo, blaqkhalif, child,eyiram1,eyiram2,ladywed, prime1,prime2,wedguy,yaw
]
</script>

<div id="portrait_card" class="grid grid-cols-2 gap-2 w-120 my-0 m-auto">
        {#each Portraits as portrait }
            <img src={portrait} alt="">
        {/each}
</div>