## Hardware knowledge

### CPU
* Good to reserve 2 threads/GPU. So with multi-thread CPU nowadays, number of CPU cores should be >= number of GPU
* CPU lane = total support for active PCI slots (GPU). E.g. 40 lane = 16x/16x || 16/16/8 || 8/8/8/8. I.e. To be able to run 8 GPU each at max 16x on 1 board, you need dual 40-lane CPUs.
* CPU lane options: 44-lane (new 6+ cores), 40-lane (modern quad-core), 28-lane, 16-lane

### Motherboard
* Watch out for supported speed of each PCI slot (x16,x8,x4) when running multiple GPUs
* Some mid to lower end boards, when an SSD M.2 port is occupied, one of the PCI slot speed is reduced.
* M.2 (M.2 PCIe) socket is the new interface for new SSD. SATA 3.0 = 600MG/s, M.2 = 1GB/s; Can use multiple M.2 socket for multiply up the speed, e.g. 2 M.2 slots = 2GB/s

### RAM
* non-ECC vs ECC: ECC = error correction code, only important for high availability system. For GPU cluster, non-ECC RAMP is fine.
* LC14/15/16 or 4 digit d-d-d-d: Latency reading from RAM itself, generally lower = better, but not too much noticeable
* RAM clock rate is irrelevant => Buy what is cheap. Buy at least as much CPU RAM as you have GPU RAM.
* DDR4 is benefit for non-deep learning ML

### Others
* Hard drive/SSD
* PSU: Add up watts of GPUs + CPU + (100-300); High efficiency rating for training large convolutional neural networks
* Cooling

## Hard selection
### Under consideration
1. Motherboard: supporting PCI x16/x16/x8
    * $120 - [ASUS X99-A/USB 3.1](https://www.asus.com/us/Motherboards/X99AUSB_31/specifications/) - [CPU/memory support](https://www.asus.com/us/Motherboards/X99AUSB_31/HelpDesk_CPU/)
    * $180 - [ASUS X99-E](https://www.asus.com/us/Motherboards/X99-E/specifications/) - [CPU/memory support](https://www.asus.com/us/Motherboards/X99-E/HelpDesk_CPU/)
    * $350 - [ASUS X99-PRO/USB 3.1](https://www.asus.com/us/Motherboards/X99PROUSB_31/specifications/)
    * $530 - [ASUS X99-E WS](https://www.asus.com/Motherboards/X99E_WS/specifications/)
2. CPU: 40 PCI lane requirement
    * $355 - [Intel Xeon E5-1620 V4](https://ark.intel.com/products/92991/Intel-Xeon-Processor-E5-1620-v4-10M-Cache-3_50-GHz)
    * $400 - [Intel Xeon E5-1650 v3](https://ark.intel.com/products/82765/Intel-Xeon-Processor-E5-1650-v3-15M-Cache-3_50-GHz)
3. RAM
    * $355 - [Corsair 32GB 2.4GHz](https://www.amazon.com/dp/B016BWEQYG)

### Purchase List
|Component|Hardware|Qty|PurchaseLink|EffectiveCost|
|:----------|:---------|:---:|:-------------|--------------:|
| CPU | [Intel Xeon E5-1620 V4](https://ark.intel.com/products/92991/Intel-Xeon-Processor-E5-1620-v4-10M-Cache-3_50-GHz) | 1 | [here](https://www.ebay.com/itm/173177773498)|$250|
| Motherboard |[ASUS X99-E](https://www.asus.com/us/Motherboards/X99-E/specifications/)|1|[Amazon](https://www.amazon.com/gp/css/summary/edit.html/ref=dp_iou_view_this_order?ie=UTF8&orderID=113-3111965-0066622)|$154|
| RAM | Corsair 32GB 3GHz (Pack-4 8GB) | 1 | |
| GPU | [Gigabyte GeForce GTX 1080 G1](http://www.gigabyte.us/Graphics-Card/GV-N1080G1-GAMING-8GD#sp)| 2 | [here](https://www.massdrop.com/buy/gigabyte-geforce-gtx-1080-g1-z370-aorus-ultra)|$1,300|
| Case | | |
| Power Supply | | |
| | | |TOTAL|$1,704| 

