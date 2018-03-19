# Create basic shapes for use with ParOSol or other tools

`basicshapes` creates shapes like cylinders, hollow cylinders and rectangles
and can also generate loadings to be used with
[ParOSol](https://github.com/reox/parosol-tu-wien) as demo/testing objects.

Note that this uses the H5 format used by ParOSol! The ordering of dimensions is
intended (by ParOSol) and not a bug!

# Examples

## Hollow cylinder in compression (1)

```
basicshapes cylinder --file hollow_cylinder_w_loading3.h5 \
                -D 31.32 -d 12.65 -H 10 \
                --voxeldim 1 --modulus 9000 --nu 0.3 \
                --loading -10.0 \
                --loading-dir 2 --loading-face top --constraint-face bottom \
                --no-base --no-top
```

## Hollow cylinder in compression (2)

```
basicshapes cylinder -D 30 -d 20 -H 64 \
                --voxeldim 0.5 --modulus 1000 --nu 0.3 \
                --file hollow3.h5 \
                --constraint-face south \
                --loading-face north \
                --loading -1000 \
                --loading-dir 1 --extrusion-dir 1 --constraint-dim 1
```

## Beam in bending

```
basicshapes box --file cubetest2.h5 \
                -L 8 -B 64 -H 8 \
                --voxeldim 0.25 --modulus 1000 --nu 0.3 \
                --loading -10.0 --loading-dir 2 \
                --loading-edge topnorth --constraint-face south
```

## Hollow cylinder in bending

```
basicshapes cylinder -H 200 -D 30 -d 20 \
                --voxeldim 0.5 --modulus 1000 --nu 0.3 \
                --file hollow.h5 \
                --constraint-face south --loading-bend north \
                --loading 200 --loading-dir 2 \
                --extrusion-dir 1 --bending-dir 0
```

## Hollow cylinder with normal distribution fill as numpy file

```
basicshapes --midplanes --file testbla.npy --format numpy \
                --fill-normal -D 30 -d 15 -H 30 \
                --voxeldim 0.1 --modulus 1 --nu 0.5 \
                --fill-mean 0.5 --fill-sd 0.2 cylinder
```
