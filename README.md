# Testing NeRFS as INRs of Depth

This is the code-base for the research paper. TBD

Important Things to Know:
`modules` contains the network modules for our case study (Gauss, SIREN, WIRE and RELU activated NeRF architectures).

`runfile.py` can be configured to run training/evaluation, generate the scene and visualise the scene

`run_load_state.py` can be used to load the state of an experiment/network and display the scene/render images of the views. (Note that we have hard coded the image rendering step. If you change the number of rays in each view/the number of views, remeber to change `trainer.disp_heat()` in `trainer.py`)

`scene.py` defines the scene handler - setting up geometries and solving the GT targets. The `Scene` class also handles the interfacing with `Trainer`.

`trainer.py` defines the training / visualisation handler - it trains given networks and visualises the 3D scene with and without predicted results.


<details>
<summary>Installation</summary>
<br>

```
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 -f https://download.pytorch.org/whl/torch_stable.html
```

![name-of-you-image](notebook_results/Test002_recoloured.png)
</details>

