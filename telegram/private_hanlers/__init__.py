from aiogram import Router

from . import post, sendfrom, logs, admin_info, ban


router = Router()

router.include_router(post.router)
router.include_router(sendfrom.router)
router.include_router(logs.router)
router.include_router(admin_info.router)
router.include_router(ban.router)
