package cn.teamthevoid.AiTankArenaServer.room;

import lombok.extern.slf4j.Slf4j;

@Slf4j
public class RoomNotFoundException extends RuntimeException {
    public RoomNotFoundException(Integer roomId) {
        super();
        log.error("room not found:{}", roomId);
    }
}
