# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.5
# ---

# %% [markdown]
# $$
# \begin{bmatrix}+\cos \theta &-\sin \theta &0\\+\sin \theta &+\cos \theta &0\\0&0&1\end{bmatrix}^T\begin{bmatrix}\sigma _{xx}&\tau _{xy}&\tau _{zx}\\\tau _{xy}&\sigma _{yy}&\tau _{yz}\\\tau _{zx}&\tau _{yz}&\sigma _{zz}\end{bmatrix}\begin{bmatrix}+\cos \theta &-\sin \theta &0\\+\sin \theta &+\cos \theta &0\\0&0&1\end{bmatrix}
# $$
# $$
# \begin{bmatrix}+\cos \theta &+\sin \theta &0\\-\sin \theta &+\cos \theta &0\\0&0&1\end{bmatrix}\begin{bmatrix}\sigma _{xx}&\tau _{xy}&\tau _{zx}\\\tau _{xy}&\sigma _{yy}&\tau _{yz}\\\tau _{zx}&\tau _{yz}&\sigma _{zz}\end{bmatrix}\begin{bmatrix}+\cos \theta &-\sin \theta &0\\+\sin \theta &+\cos \theta &0\\0&0&1\end{bmatrix}
# $$
# $$
# \begin{bmatrix}+\sigma _{xx}\cos \theta +\tau _{xy}\sin \theta &+\tau _{xy}\cos \theta +\sigma _{yy}\sin \theta &+\tau _{zx}\cos \theta +\tau _{yz}\sin \theta \\-\sigma _{xx}\sin \theta +\tau _{xy}\cos \theta &-\tau _{xy}\sin \theta +\sigma _{yy}\cos \theta &-\tau _{zx}\sin \theta +\tau _{yz}\cos \theta \\\tau _{zx}&\tau _{yz}&\sigma _{zz}\end{bmatrix}\begin{bmatrix}+\cos \theta &-\sin \theta &0\\+\sin \theta &+\cos \theta &0\\0&0&1\end{bmatrix}
# $$
# $$
# \begin{bmatrix}+\sigma _{xx}\cos \theta \cos \theta +\tau _{xy}\sin \theta \cos \theta +\tau _{xy}\sin \theta \cos \theta +\sigma _{yy}\sin \theta \sin \theta &-\sigma _{xx}\sin \theta \cos \theta -\tau _{xy}\sin \theta \sin \theta +\tau _{xy}\cos \theta \cos \theta +\sigma _{yy}\sin \theta \cos \theta &+\tau _{zx}\cos \theta +\tau _{yz}\sin \theta \\-\sigma _{xx}\sin \theta \cos \theta +\tau _{xy}\cos \theta \cos \theta -\tau _{xy}\sin \theta \sin \theta +\sigma _{yy}\sin \theta \cos \theta &+\sigma _{xx}\sin \theta \sin \theta -\tau _{xy}\sin \theta \cos \theta -\tau _{xy}\sin \theta \cos \theta +\sigma _{yy}\cos \theta \cos \theta &-\tau _{zx}\sin \theta +\tau _{yz}\cos \theta \\+\tau _{zx}\cos \theta +\tau _{yz}\sin \theta &-\tau _{zx}\sin \theta +\tau _{yz}\cos \theta &\sigma _{zz}\end{bmatrix}
# $$
