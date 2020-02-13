package cn.teamthevoid.AiTankArenaServer.handler.websocket;

import io.netty.buffer.ByteBuf;
import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.codec.MessageToMessageDecoder;
import io.netty.handler.codec.http.websocketx.BinaryWebSocketFrame;

import java.util.List;

public class WebSocketBinaryDataDecoder extends MessageToMessageDecoder {
    @Override
    protected void decode(ChannelHandlerContext ctx, Object msg, List out) throws Exception {
        ByteBuf buf = ((BinaryWebSocketFrame) msg).content();
        out.add(buf);
        buf.retain();
    }
}
