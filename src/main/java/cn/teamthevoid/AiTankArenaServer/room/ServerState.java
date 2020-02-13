package cn.teamthevoid.AiTankArenaServer.room;

import cn.teamthevoid.AiTankArenaServer.game.Player;
import io.netty.channel.Channel;
import io.netty.util.AttributeKey;
import lombok.extern.slf4j.Slf4j;

import java.util.HashMap;
import java.util.Optional;


@Slf4j
public class ServerState {
    public static AttributeKey<Room> ROOM = AttributeKey.valueOf("room");
    public static AttributeKey<Player> PLAYER = AttributeKey.valueOf("player");
    private HashMap<Integer, Room> roomMap = new HashMap<>();//roomID -> Session

    public ServerState() {
        log.info("Create Debug room:" + createRoom());
    }

    //返回SessionID
    public Integer createRoom() {
        var newRoom = new Room();
        roomMap.put(newRoom.getID(), newRoom);
        log.info("new room:" + newRoom.getID());
        return newRoom.getID();
    }

    public Room getRoom(Integer roomID) {
        return roomMap.get(roomID);
    }

    public void exitRoom(Player player) {
        roomMap.remove(player);
    }

    //返回PlayerID
    public Integer joinRoom(Integer roomID, Channel channel, Player player) {
        return Optional
                .ofNullable(getRoom(roomID))
                .orElseThrow(() -> new RoomNotFoundException(roomID))
                .join(channel, player);

    }

    public Room getMyRoom(Channel channel) {
        return channel.attr(ROOM).get();
    }

    public Player getSelf(Channel channel) {
        return channel.attr(PLAYER).get();
    }


}
