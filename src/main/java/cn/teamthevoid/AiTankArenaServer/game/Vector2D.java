package cn.teamthevoid.AiTankArenaServer.game;

import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@AllArgsConstructor

public class Vector2D {
    public float x;
    public float y;

    public Vector2D(cn.teamthevoid.AiTankArenaServer.message.operation.Vector2D vector2D) {
        this.x = vector2D.getX();
        this.y = vector2D.getY();
    }

    public Vector2D add(Vector2D vector) {
        Vector2D result = this.clone();
        result.x += vector.x;
        result.y += vector.y;
        return result;
    }

    //数乘
    public Vector2D scale(float a) {
        Vector2D result = this.clone();
        result.x *= a;
        result.y *= a;
        return result;
    }

    //获取模长
    public float getMagnitude() {
        return (float) Math.sqrt(x * x + y * y);
    }

    //获取单位向量
    public Vector2D normalize() {
        Vector2D result = this.clone();
        double magnitude = getMagnitude();
        result.x /= magnitude;
        result.y /= magnitude;
        return result;
    }

    @Override
    protected Vector2D clone() {
        return new Vector2D(this.x, this.y);
    }
}
