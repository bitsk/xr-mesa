# xr-mesa

独立维护的 XR 源码补丁栈与 openKylin 打包入口。

本仓库保存实际功能补丁、上游提交锁定和构建配方。`tools/prepare-source.py` 检出真实上游，在其历史之上逐条应用功能提交；`packaging/build-debs.sh` 在准备后的源码中构建独立软件包。完整上游历史由锁定的上游获取，本仓库的 Git 历史管理适配补丁与打包变更。

离线准备可传 `--upstream-repo /path/to/local/upstream`，或设置 XR_UPSTREAM_REPO。实际内核、模块、DTB、图形选择及设备功能分别验收。源码准备和包构建不自动刷写设备或替换系统活动图形栈。

FDM 补丁开放现有 CPU 解码路径支持的 `R8G8_UNORM` 密度图格式，应用仍须显式启用对应功能。A650 的跨进程 OpenXR 验证采用非 subsampled 颜色交换链；主动请求 subsampled 存储的路径出现重构接缝，不能仅凭 GPU 时间下降选用。此补丁不修改应用分辨率、畸变或全局 FFR 默认值。
