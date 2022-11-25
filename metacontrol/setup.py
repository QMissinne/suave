from setuptools import setup

package_name = 'metacontrol'

setup(
    name=package_name,
    version='0.23.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jeroen',
    maintainer_email='j.zwanepol@hotmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'spiral_lc_node = metacontrol.spiral_lc_node:main',
            'talker_lc_node = metacontrol.talker_lc_node:main',
        ],
    },
)
