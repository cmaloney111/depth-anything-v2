import setuptools

requirements = [
    "torch",
    "torchvision",
    "opencv-python",
]

setuptools.setup(
    name="depth_anything_v2",
    version="0.0.1",
    python_requires=">=3.9",  
    packages=["depth_anything_v2", "depth_anything_v2.dinov2_layers", "depth_anything_v2.util"],
    install_requires=requirements,
)
