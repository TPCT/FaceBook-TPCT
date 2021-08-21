<?php
    class FACEBOOKAPI{
        private ?string $url = "https://m.facebook.com";
        private ?string $username = "";
        private ?string $password = "";
        private ?string $useragent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)';
        private bool $logged = false;
        private $domHtml;
        private $resource;

        public function __construct($username, $password, $useragent=null){
            $this->resource = curl_init();
            $this->username = $username;
            $this->password = $password;
            $useragent ??= $this->useragent;
            curl_setopt_array($this->resource, [
                CURLOPT_URL => $this->url,
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_FOLLOWLOCATION => true,
                CURLOPT_USERAGENT => $useragent,
                CURLOPT_COOKIEFILE => __DIR__ . '/cookies.txt',
                CURLOPT_COOKIEJAR => __DIR__ . '/cookies.txt',
                CURLINFO_HEADER_OUT => true
            ]);
            $this->domHtml = new DOMDocument();
        }

        public function login(): bool{
            $post_fields = ["email" => $this->username,
                            "pass" => $this->password];

            $data = curl_exec($this->resource) or die($this->resource);

            if ($data){
                $this->domHtml->loadHTML($data);
                $form = $this->domHtml->getElementsByTagName('form')->item(0);
                $this->url .= $form->getAttribute('action');
                
                foreach($form->getElementsByTagName('input') as $input){
                        $fieldName = $input->getAttribute('name');
                        $fieldValue = $input->getAttribute('value');
                        if ($fieldName && !in_array($fieldName, array_keys($post_fields)))
                            $post_fields[$fieldName] = $fieldValue;
                }

                curl_setopt($this->resource, CURLOPT_URL, $this->url);
                curl_setopt($this->resource, CURLOPT_POST, true);
                curl_setopt($this->resource, CURLOPT_POSTFIELDS, $post_fields);
                
                $data = curl_exec($this->resource);
                $this->domHtml->loadHTML($data);
                if (!$this->domHtml->getElementById('login_error')){
                    $this->logged = true;
                }

            }
            return $this->logged;
        }

        public function __destruct()
        {
            curl_close($this->resource);
            unset($this->domHtml);
        }
    }
?>
