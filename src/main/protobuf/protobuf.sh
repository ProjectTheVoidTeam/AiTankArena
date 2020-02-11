#rm -rf ../java/message/
protoc -I=./ --java_out=../java/ --python_out=../python/ --csharp_out=../unity/Assets/Script/Protobuf ./*.proto
#cp ./*.proto ../javascript/protobuf