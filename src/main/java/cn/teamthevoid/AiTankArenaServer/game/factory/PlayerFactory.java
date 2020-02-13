package cn.teamthevoid.AiTankArenaServer.game.factory;

import cn.teamthevoid.AiTankArenaServer.game.Player;
import cn.teamthevoid.AiTankArenaServer.game.impl.PlayerImpl;

public class PlayerFactory {
    public static Player getNewInstance() {
        return new PlayerImpl();
    }
}
