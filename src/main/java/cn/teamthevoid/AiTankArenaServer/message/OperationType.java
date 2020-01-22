// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: operation.proto

package cn.teamthevoid.AiTankArenaServer.message;

/**
 * <pre>
 * option java_outer_classname = "Grpc";
 * </pre>
 * <p>
 * Protobuf enum {@code AiTankArenaServer.OperationType}
 */
public enum OperationType
        implements com.google.protobuf.ProtocolMessageEnum {
  /**
   * <pre>
   * 获取状态
   * </pre>
   *
   * <code>GET_STATUS = 0;</code>
   */
  GET_STATUS(0),
  /**
   * <pre>
   * 加入战局
   * </pre>
   *
   * <code>JOIN = 1;</code>
   */
  JOIN(1),
  /**
   * <pre>
   * 提交AI行动
   * </pre>
   *
   * <code>AI_ACTION = 2;</code>
   */
  AI_ACTION(2),
  /**
   * <pre>
   * 认输
   * </pre>
   *
   * <code>FRANCE = 3;</code>
   */
  FRANCE(3),
  /**
   * <pre>
   * 本回合挂机
   * </pre>
   *
   * <code>HALT = 4;</code>
   */
  HALT(4),
  /**
   * <pre>
   * 开局时选择装备
   * </pre>
   *
   * <code>INIT = 5;</code>
   */
  INIT(5),
  /**
   * <pre>
   * 重连
   * </pre>
   *
   * <code>REJOIN = 6;</code>
   */
  REJOIN(6),
  /**
   * <pre>
   * 获取服务器信息
   * </pre>
   *
   * <code>SERVER_INFO = 7;</code>
   */
  SERVER_INFO(7),
  UNRECOGNIZED(-1),
  ;

  /**
   * <pre>
   * 获取状态
   * </pre>
   *
   * <code>GET_STATUS = 0;</code>
   */
  public static final int GET_STATUS_VALUE = 0;
  /**
   * <pre>
   * 加入战局
   * </pre>
   *
   * <code>JOIN = 1;</code>
   */
  public static final int JOIN_VALUE = 1;
  /**
   * <pre>
   * 提交AI行动
   * </pre>
   *
   * <code>AI_ACTION = 2;</code>
   */
  public static final int AI_ACTION_VALUE = 2;
  /**
   * <pre>
   * 认输
   * </pre>
   *
   * <code>FRANCE = 3;</code>
   */
  public static final int FRANCE_VALUE = 3;
  /**
   * <pre>
   * 本回合挂机
   * </pre>
   *
   * <code>HALT = 4;</code>
   */
  public static final int HALT_VALUE = 4;
  /**
   * <pre>
   * 开局时选择装备
   * </pre>
   *
   * <code>INIT = 5;</code>
   */
  public static final int INIT_VALUE = 5;
  /**
   * <pre>
   * 重连
   * </pre>
   *
   * <code>REJOIN = 6;</code>
   */
  public static final int REJOIN_VALUE = 6;
  /**
   * <pre>
   * 获取服务器信息
   * </pre>
   *
   * <code>SERVER_INFO = 7;</code>
   */
  public static final int SERVER_INFO_VALUE = 7;
  private static final com.google.protobuf.Internal.EnumLiteMap<
          OperationType> internalValueMap =
          new com.google.protobuf.Internal.EnumLiteMap<OperationType>() {
            public OperationType findValueByNumber(int number) {
              return OperationType.forNumber(number);
            }
          };
  private static final OperationType[] VALUES = values();
  private final int value;

  private OperationType(int value) {
    this.value = value;
  }

  /**
   * @param value The numeric wire value of the corresponding enum entry.
   * @return The enum associated with the given numeric wire value.
   * @deprecated Use {@link #forNumber(int)} instead.
   */
  @java.lang.Deprecated
  public static OperationType valueOf(int value) {
    return forNumber(value);
  }

  /**
   * @param value The numeric wire value of the corresponding enum entry.
   * @return The enum associated with the given numeric wire value.
   */
  public static OperationType forNumber(int value) {
    switch (value) {
      case 0:
        return GET_STATUS;
      case 1:
        return JOIN;
      case 2:
        return AI_ACTION;
      case 3:
        return FRANCE;
      case 4:
        return HALT;
      case 5:
        return INIT;
      case 6:
        return REJOIN;
      case 7:
        return SERVER_INFO;
      default:
        return null;
    }
  }

  public static com.google.protobuf.Internal.EnumLiteMap<OperationType>
  internalGetValueMap() {
    return internalValueMap;
  }

  public static final com.google.protobuf.Descriptors.EnumDescriptor
  getDescriptor() {
    return cn.teamthevoid.AiTankArenaServer.message.OperationOuterClass.getDescriptor().getEnumTypes().get(0);
  }

  public static OperationType valueOf(
          com.google.protobuf.Descriptors.EnumValueDescriptor desc) {
    if (desc.getType() != getDescriptor()) {
      throw new java.lang.IllegalArgumentException(
              "EnumValueDescriptor is not for this type.");
    }
    if (desc.getIndex() == -1) {
      return UNRECOGNIZED;
    }
    return VALUES[desc.getIndex()];
  }

  public final int getNumber() {
    if (this == UNRECOGNIZED) {
      throw new java.lang.IllegalArgumentException(
              "Can't get the number of an unknown enum value.");
    }
    return value;
  }

  public final com.google.protobuf.Descriptors.EnumValueDescriptor
  getValueDescriptor() {
    return getDescriptor().getValues().get(ordinal());
  }

  public final com.google.protobuf.Descriptors.EnumDescriptor
  getDescriptorForType() {
    return getDescriptor();
  }

  // @@protoc_insertion_point(enum_scope:AiTankArenaServer.OperationType)
}

