package cn.teamthevoid.AiTankArenaServer.game.impl;

import cn.teamthevoid.AiTankArenaServer.game.Tank;
import cn.teamthevoid.AiTankArenaServer.game.Vector2D;

public class TankImpl extends Tank {
    public Vector2D position = new Vector2D(0, 0);

    public TankImpl(Vector2D initPostion) {
        super(initPostion);
    }

    @Override
    public Vector2D getPosition() {
        return this.position;
    }

    @Override
    public void move(Vector2D direction, float speed) {
        position = position.add(direction.scale(speed));


    }
}
